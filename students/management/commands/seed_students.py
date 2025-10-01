from typing import Any
from django.core.management.base import BaseCommand
import random
from students.models import Student


class Command(BaseCommand):
    help = "Add sample students to database"

    def handle(self, *args: Any, **options: Any) -> str | None:

        first_names = [
            "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
            "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
            "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
            "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
            "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
            "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
            "Edward", "Deborah"
        ]

        last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
            "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
            "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
            "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
            "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
            "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter"
        ]

        nicknames = [
            "Ace", "Bear", "Champ", "Duke", "Flash", "Jazz", "Kit", "Maverick", "Ninja", "Oz",
            "Pip", "Rocky", "Scout", "Tex", "Viper", "Wolf", "Ziggy", "Buzz", "Dash", "Echo",
            "Finn", "Gizmo", "Hawk", "Indy", "Jax", "Koda", "Lucky", "Mojo", "Nova", "Otis",
            "Pax", "Quinn", "Rex", "Sky", "Taz", "Uno", "Vega", "Wren", "Yogi", "Zane",
            "Blue", "Coco", "Daisy", "Frost", "Goldie", "Honey", "Ivy", "Juno", "Luna", "Misty"
        ]

        for _ in range(100):
            first = random.choice(first_names)
            last = random.choice(last_names)
            nick = random.choice(nicknames)
            Student.objects.create(first_name=first, last_name=last, nickname=nick)        
        self.stdout.write(self.style.SUCCESS("Successfully seeded database with students"))