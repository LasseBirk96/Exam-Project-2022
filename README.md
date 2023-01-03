# Exam Project 2022


## Brief System Walk-through


The system is essentially a lesser version of the food delivery website "Just-Eat". 
The system architecture is microservice-oriented, meaning that rather than having one large monolithic system, it has multiple smaller systems or services that are responsible for handling specific tasks. In the diagram below we can see how the system is currently setup. The client interacts with an API-gateway redirecting them to the correct services' API. It is worth noting that despiste the diagram having a "presentation layer", no front-end has been developed as there wasn't enough time to do so. However should a front-end developed in the future, the setup would remain the same.


<img width="656" alt="image" src="https://user-images.githubusercontent.com/56427491/208114384-6d4f3aaf-5581-4abc-ac74-7b47d1d65971.png">

In its current iteration the system has 5 different components.

**The Driver Component**, this component is responsible for handling everything related to drivers. Drivers can be created, can login into their own account, can view orders that they can choose to deliver, and view the points they have accumalted from successfully deliviering orders.


**The User Component**, this component deals with the user or client aspect of our food delivery website. 
A user can register, login, and via the order component make new orders, and see current and old orders.


**The Product Component**, the product component allows administrators to create and delete items of the menu, as well as allowing users to be able to view products for ordering.


**The Order Component**, the component deals with the creation of orders, deletion of orders, and history of orders. This component also deals with the delivery of the order and uses the Google Maps API to track the time an order should take to deliver, as well as the actual time the delivery took to deliver.


**The Banking Component**, this component is meant to mock a bank or other form of payment service. It's inclusion is purely for proof of concept rather than any actual useful functionality in a real busines scenario. However, in our case it is meant to verify if a user can pay for an order before that order is accepted.


It is important to note that not all functionality has been developed as of writing this documentation, it is more of a display of considerations and ideas that could relatively easily be implemented in the future and may be implemented before the oral exam.


All components are build the same way internally. There is a database layer and a logic layer, also present are logging and test modules. The database layer is responsible for handling database transactions, whilst the logic layer is responsible for handling API-requests as well as input sanitation and minor security features. The entire component is run by the "main.py" file, that boots up a flask server that allows the component to communicate with other API's and services, we consider this to be the top layer. The entire system is setup in a CI/CD pipeline that checkouts the code base, runs and validates tests, and finally builds the code. While there are some minor differences, every component is build nearly the same way in order to allow for easy expansion. Pictured below is a diagram of our user component, we will be using this to demonstrate how a component functions.

<img width="1038" alt="image" src="https://user-images.githubusercontent.com/56427491/208118412-d1afb208-7dcd-473e-bbd8-c1c05af990a1.png">

We admit that this diagram can be a bit confusing to follow, so we will provide a quick tour of the component using the numbers.



1. As mentioned earlier this is where the component actually runs. A flask server gets booted and initialises the API and the rest of the system.

2. The API in it self is located in the "user_api.py" file. Here various endpoints are located and future ones can easily be added. The data that gets send to an endpoint is immediality send to an instance of the "Handler.py" class. This is where the request gets handled and dealt with properly. All requests are sanitized for various malware, and is then shipped of to the database layer.

3. In the database layer we find "user_queries.py" that contains all queries used to communicate with the database. Connections get established and sensitive data gets hashed. Relevant information about the transaction is then returned to the client. For example, whether or not an error occured or if everything went as planned.

4. This is our test folder, and while the diagram doesn't show excactly what things are being testing, essentially this our test suite where various methods and functionality is tested. This is not relevant once the component is deployed, only during development and CI/CD.

5. This module is for logging, which makes debugging and error handling more manageable. 

6. It might seem weird that our main file goes directly into the database layer, and we agree. This is purely for being able to demonstrate the component locally more easily, and this "functionality" should be removed upon any serious deployment.

7. This is our requirement file, that is used when building the component in our CI/CD.

## Integration Development And Considerations
The system has been developed using various agile methods such as Scrum and XP. One component of the system was created at a time and was then connected to the other components of the system after creation. The entire point of the integration design is that a component can easily be removed, updated, or added, without having any effect on the functionality of the other components. Other relevant design considerations have been mentioned in the video for this exam.


