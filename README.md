# SystemsDesignIntervew

Systems Design Interview For IT Taxi App like Uber or Cabify

Design a scalable system architecture in the cloud for global taxis business around the world in major cities of the world, in total its more than 11.000 cars worldwide. Our taxis are operating every day 24 hours and complete small or large trips throughout the day. 

From our headquarters we have to ensure many things in order to run the business,
1. We have to ensure receipts are generated for every trip
2. Our management can review various metrics from the trips 
    1. revenue per city
    2. length of the trips
    3. Other
3. We should be able to prevent fraud
4. Plan where we place our taxis within the city throughout the day.

## Assignment:

1. Architecture: Design an achitecture that allows us to collect, process and analyze data from our taxi operation as well as send data back to individual cars and communicate with our users. 

2. Automation Develop script to automate the setup and maintenance of your architecture. Its ok if its only parts of it or 2-3 components and not the whole architecture.  We should be able: to rollout the components or microservices and also update the whole or the individual parts of it. 

3. Data Exfiltration and Infiltration: Think about how to secure the data we are collecting for this use case and the platform in general. What tools and approaches can be used to minimize the risk of unwanted Data Exfiltration or Data Infiltration that is stored in the cloud

4. Vision: Create a vision for the future of our taxi company data platform, what are going to be important pillars and elements that we should focus on in the next 2-3 years 


## Implicit Functional Requirments
### Core
- Riders should be able get a fare estimate of the trip based on the input source location and a destination location.
- Riders should be able to request a ride based on the estimated fare. 
- Riders should be matched with a driver who is nearby and available upon request.
- Drivers should be able to accept/decline a request.
- Drivers should navigate to pickup/drop-off location.

## Functional Requirments 
### Core
- The system should store and generat a unique receipt for each completed trip.
- Business Managers should be able to view and analyse metrics from the trip souch as length of each trips and revenue per city.
- The system should perform fraud detection based on customers information and trip data to flagg it for manual review. 
- The system should perform suggestions of City areas where to be for Drivers based on there current location, real time data of other Drivers (suply) and Riders (demand). 



### Out of scope requirments 
- Riders should be able to create there account, verify the email and phone, add personal information, payment method, sing the contract, get verivied and more. 
- Drivers should be able to create there account, add personal information, taxi lisence sign contract, get verified and more. 
- Riders and Drivers should be able to comunicate via chat or call once the ride is accepted.
- Riders should be able to rate their Rides and Drivers after the.
- Drivers should be able to rate Riders after the trip.
- Riders should be able to schedule rides in advance.
- Riders should be able to request different categories of cars.
- The system should be able to accept multiple payment methods and gateways, not only cash(visa, mastercard, amex, ....)
- The system should be able to send a unique receipt for each completed trip to the Rider and Driver. 
- Business Managers should be able to review and verify to aprove or deny every Drivers request.
- Business Managers should be able to block and restrict access to Riders and Drivers.
- Business Managers should be able to view and analyse metrics from the trip souch as pick hours, pick locations, and others
- The system shall allow management to view and act on flagg as fraud trips. 
- The system shall allow management to define and adjust fraud detection rules. 



## Non-Functional Requirments
### Core Requirements
- The system should ensure the security and privacy of user and driver data, complying with regulations in like GDPR in Europe.
-  The system should facilitate easy setup, updates, maintenance and roll out of each service without significant downtime.
- The system shall ingest real-time data (GPS, trip status updates) from all 11,000+ taxis with with low latency especialy during peack hours.
- Mechanisms shall be in place to prevent accidental or intentional exfiltration (Data Loss Prevention) of sensitive data.
- The architecture shall be designed to scale verticaly and horizontally for all critical components or services to handle increasing data volume, user traffic, and the potential addition of more taxis.



### Out of scope
- The system should have Strict SLO and SLI for Performance, Availability, Security, Data Integrity, Maintainability, ...
- The system should be resilient to failures, with redundancy and failover mechanisms in place.
- The system should be able to handle high throughput, especially during peak hours or special events 
- The system shall be able to automatically scale resources up or down based on demand fluctuations.
- The data lake and data warehouse shall be capable of storing and efficiently querying petabytes of data.
- The system should have robust monitoring, logging, and alerting to quickly identify and resolve issues.
   



## Sources 
- https://medium.com/@karan99/system-design-uber-33593137a4fe 
- https://www.geeksforgeeks.org/system-design-of-uber-app-uber-system-architecture/ 
- https://medium.com/nerd-for-tech/uber-architecture-and-system-design-e8ac26690dfc
- https://www.uber.com/en-ES/blog/architecture-api-gateway/ 
https://www.uber.com/en-ES/blog/tech-stack-part-one-foundation/
- https://www.uber.com/en-ES/blog/microservice-architecture/
- https://theappsolutions.com/blog/development/uber-tech-stack/