import math


# Kalkulator Figur Geometrycznych:
# Zaimplementuj klasę Shape, która będzie bazą dla różnych figur geometrycznych.
# Następnie utwórz podklasy dla konkretnych figur, takich jak Circle, Rectangle i Triangle.
# Każda z tych klas powinna mieć metody do obliczania pola powierzchni oraz obwodu.
class Shape:
    def get_perimeter(self):
        raise NotImplemented()

    def get_area(self):
        raise NotImplemented()


class Circle(Shape):

    def init(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * self.radius * 3.14

    def get_area(self):
        return 3.14 * (self.radius * self.radius)


class Rectangle(Shape):

    def init(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b


class Triangle(Shape):

    def init(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return sum([self.a, self.b, self.c])

    def get_area(self):
        s = self.get_perimeter() / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


# System Zarządzania Zadaniem:
# Stwórz klasę Task, która reprezentuje zadanie do wykonania. Klasa powinna przechowywać
# informacje takie jak opis zadania, priorytet, termin wykonania itp. Następnie utwórz
# klasę TaskManager, która będzie zarządzać listą zadań. Użytkownik powinien mieć możliwość
# dodawania, usuwania i przeglądania zadań.
from datetime import datetime


class Task:
    def init(self, description, priority, deadline):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.created_at = datetime.now()

    def str(self):
        return (f"Description: {self.description}, Priority: {self.priority}, "
                f"Deadline: {self.deadline}, Created At: {self.created_at}")


class TaskManager:
    def init(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task.description}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task removed: {removed_task.description}")
        else:
            print("Invalid task index")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"Task {idx + 1}: {task}")


# Dla chętnych:
# System Rezerwacji Biletów:
# Stwórz klasę Event, która reprezentuje wydarzenie (np. koncert, seans filmowy).
# Następnie stwórz klasę Ticket, która reprezentuje bilet na to wydarzenie.
# Klasa Ticket powinna być powiązana z klasą Event, a użytkownicy powinni mieć
# możliwość rezerwacji biletów na dane wydarzenie.
class Event:
    def init(self, name, date, location, total_tickets):
        self.name = name
        self.date = date
        self.location = location
        self.total_tickets = total_tickets
        self.booked_tickets = 0

    def book_ticket(self):
        if self.booked_tickets < self.total_tickets:
            self.booked_tickets += 1
            return True
        else:
            return False

    def str(self):
        return (f"Event: {self.name}, Date: {self.date}, Location: {self.location}, "
                f"Total Tickets: {self.total_tickets}, Booked Tickets: {self.booked_tickets}")


class Ticket:
    def init(self, event):
        if event.book_ticket():
            self.event = event
            self.ticket_number = event.booked_tickets
            print(f"Ticket booked successfully for event: {event.name}, Ticket Number: {self.ticket_number}")
        else:
            self.event = None
            self.ticket_number = None
            print("Failed to book ticket: No available tickets")

    def str(self):
        if self.event:
            return (f"Ticket Number: {self.ticket_number}, Event: {self.event.name}, "
                    f"Date: {self.event.date}, Location: {self.event.location}")
        else:
            return "Invalid Ticket"
