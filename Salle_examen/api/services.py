from django.utils import timezone
from datetime import timedelta, time, datetime
from Session.models import Session
from Examen.models import Examen
from Salle.models import Salle
from Salle_examen.models import Salle_examen
from django.db import IntegrityError

def affectation_examens_salles(session_id=None):
    if session_id:
        session = Session.objects.filter(id_session=session_id).first()
        if not session:
            print(f"Aucune session trouvée avec l'ID {session_id}.")
            return
    else:
        session = Session.objects.first()  # Par défaut, on choisit la première session si aucune session n'est spécifiée

    if not session:
        print("Aucune session trouvée.")
        return

    current_date = session.date_d
    today = timezone.now().date()

    # Réinitialiser la disponibilité des salles
    Salle.objects.update(dispo=True)

    # Supprimer les objets Salle_examen existants
    Salle_examen.objects.all().delete()

    exams = Examen.objects.filter(id_session=session).order_by('type_examen', '-nbrclasse')

    if not exams.exists():
        print(f"Aucun examen trouvé pour la session {session}.")
        return

    while current_date <= session.date_f:
        if current_date.weekday() in [5, 6]:  # Ignorer les week-ends
            current_date += timedelta(days=1)
            continue

        available_rooms = Salle.objects.filter(dispo=True)

        # Assigner les examens pratiques
        for exam in exams.filter(type_examen='pratique'):
            assigned_classes = Salle_examen.objects.filter(id_examen=exam).count()  # Compter les classes déjà assignées

            for _ in range(exam.nbrclasse - assigned_classes):  # Ne pas assigner plus que le nécessaire
                if available_rooms.exists():
                    room = available_rooms.first()
                    exam_time = timezone.make_aware(datetime.combine(current_date, time(9, 0)))

                    try:
                        Salle_examen.objects.create(
                            id_salle=room,
                            id_examen=exam,
                            date_salle=exam_time
                        )
                        room.dispo = False
                        room.save()
                        available_rooms = available_rooms.exclude(id_salle=room.id_salle)
                    except IntegrityError as e:
                        print(f"Erreur d'intégrité pour l'examen {exam} dans la salle {room}: {e}")
                else:
                    print("Pas assez de salles disponibles pour les examens pratiques.")
                    break

        # Assigner les examens théoriques
        exam_time = timezone.make_aware(datetime.combine(current_date, time(9, 0)))

        for exam in exams.filter(type_examen='theorique'):
            assigned_classes = Salle_examen.objects.filter(id_examen=exam).count()  # Compter les classes déjà assignées

            for _ in range(exam.nbrclasse - assigned_classes):  # Ne pas assigner plus que le nécessaire
                if exam_time.time() < time(17, 0):
                    available_rooms = Salle.objects.filter(dispo=True)

                    if available_rooms.exists():
                        room = available_rooms.first()

                        try:
                            Salle_examen.objects.create(
                                id_salle=room,
                                id_examen=exam,
                                date_salle=exam_time
                            )
                            exam_time += timedelta(hours=2)
                            room.dispo = True

                        except IntegrityError as e:
                            print(f"Erreur d'intégrité pour l'examen {exam} dans la salle {room}: {e}")
                    else:
                        print("Pas de salles disponibles pour cet examen théorique.")
                        break
                else:
                    print("L'heure d'examen théorique dépasse la limite de 17h.")
                    break

        current_date += timedelta(days=1)

    print(f'Examens affectés aux salles pour la session {session.nom_session} avec succès.')
