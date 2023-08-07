Scenario 
You are part of a team at Data Axle that is tasked with building a system for Train Seat Reservations.

Task

Your task is to implement a small part of the backend API using Django/flask with business logic along with associated test cases that verify that the logic works according to the use cases below

Description:

The train seat reservation system is designed to allow families to reserve seats in the same cabin based on the number of members in the family. The system should ensure that all family members are seated together to provide a comfortable travel experience.
 
Use Case Flow:
 
1. The user initiates the seat reservation process for their family.
2. The system prompts the user to enter the number of family members travelling.
3. The user enters the number of family members.
4. The system checks the availability of seats on the train.
5. If there are enough seats available in the same cabin to accommodate the family, proceed to step 7.
6. If there are not enough seats available in the same cabin, the system suggests alternative options or notifies the user that the desired number of seats is not available.
7. The system prompts the user to select their preferred cabin class (e.g., first class, second class).
8. The user selects their preferred cabin class.
9. The system retrieves the seat numbers for the selected cabin class.
10. Based on the number of family members, the system determines the number of seats required and finds a suitable arrangement to accommodate the entire family in the same cabin.
11. The system reserves the seats for the family members in the selected cabin.
12. The system generates a unique reservation ID and provides it to the user.
13. The system updates the seat availability and marks the reserved seats as occupied.
14. The system displays the reservation details, including the cabin number, seat numbers, and the total fare for the reservation.
15. The user receives reservation details and payment links.
 

Feel free to make your assumptions and move forward in case you are stuck at some point in terms of requirements.
