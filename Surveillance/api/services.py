from django.utils.timezone import now 
from Surveillance.models import Surveillance
from Salle.models import Salle
from Examen.models import Examen
from Users.models import AppUser
from Contrainte.models import Contrainte
from Salle_examen.models import Salle_examen
import random

def assign_profs_to_surveillance():
    # Clear existing surveillances
    Surveillance.objects.all().delete()

    created_records = 0  # Counter for created records

    # Create a dictionary to track the number of surveillances per professor
    profs_surveillance_count = {prof.user_id: 0 for prof in AppUser.objects.all()}

    salles_examens = Salle_examen.objects.all()  # Get all `Salle_examen` instances
    print(f"Number of SALLE EXAMEN: {salles_examens.count()}")

    for salle_examen in salles_examens:  # Use a different variable name here
        # Get all available professors with constraints
        contraintes = Contrainte.objects.all()
        profs_disponibles = list(
            AppUser.objects.exclude(surveillance__date_surveillance=salle_examen.date_salle)
            .exclude(role__in=['employe', 'directeur des études', 'chef département'])
            .distinct()
        )

        # Filter professors based on constraint periods
        for contrainte in contraintes:
            if contrainte.date_debut_contrainte <= salle_examen.date_salle <= contrainte.date_fin_contrainte:
                # Exclude professors with overlapping constraints
                profs_disponibles = [prof for prof in profs_disponibles if prof.user_id != contrainte.id_user.user_id]

            # Apply specific constraints (like 'enceinte' or 'conge')
            if contrainte.nom_contrainte == 'enceinte':
                profs_disponibles = [prof for prof in profs_disponibles if prof.user_id != contrainte.id_user.user_id]
            elif contrainte.nom_contrainte == 'conge':
                profs_disponibles = [prof for prof in profs_disponibles if prof.user_id != contrainte.id_user.user_id]

        if profs_disponibles:
            # Prioritize professors with fewer surveillances
            profs_disponibles.sort(key=lambda prof: profs_surveillance_count[prof.user_id])

            # Determine the number of professors to assign (between 1 and 2)
            num_profs_to_assign = min(len(profs_disponibles), random.randint(1, 2))  # Change max to 2
            
            assigned_profs = []
            
            for _ in range(num_profs_to_assign):
                if profs_disponibles:
                    prof = profs_disponibles.pop(0)  # Get the professor with the fewest surveillances
                    Surveillance.objects.create(
                        date_surveillance=salle_examen.date_salle,
                        id_salle=salle_examen.id_salle,
                        user_id=prof  # Use user_id if that’s the field name for the foreign key to AppUser
                    )
                    created_records += 1

                    # Update the surveillance count for the professor
                    profs_surveillance_count[prof.user_id] += 1
                    assigned_profs.append(prof)

            print(f"Created surveillances for Profs: {[prof.user_id for prof in assigned_profs]}, Salle: {salle_examen.id_salle}, Total surveillances: {[profs_surveillance_count[prof.user_id] for prof in assigned_profs]}")

    print(f"Number of records created: {created_records}")

