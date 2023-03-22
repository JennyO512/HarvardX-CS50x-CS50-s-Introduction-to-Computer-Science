In a file called log.sql insert the following:
--Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports
WHERE year = 2021 and month = 7 and street = "Humphrey Street";

--result: Shoplifting took place at 04:45. Two people witnessed the event.                                                                                                                                                         |
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- Littering took place at 16:36. No known witnesses.                                                                                                                                                                       |
-- Littering took place at 17:49. Two people witnessed the event. end of result>

--select the interviews from the people that day where they may have mentioned bakery
SELECT transcript FROM interviews
WHERE year =2021 and month = 7 and day = 28 and
transcript LIKE "%bakery%";

--transcript/interview #1
--Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--If you have security footage from the bakery parking lot,
--you might want to look for cars that left the parking lot in that time frame.

--query name for possible suspects
SELECT name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
where year = 2021 and month = 7 and day = 28 and minute >= 15 AND minute <= 25 and activity = "exit";
    --suspects are: WAYNE, JORDAN, MICHAEL, VANESSA, BRUCE, BARRY, LUCA, SOFIA, IMAN, DIANA, KELSEY, ETHAN Vincent Sophia, Jeremy, Brandon


--transcript/interview #2
--I don't know the thief's name, but it was someone I recognized.
--Earlier this morning, before I arrived at Emma's bakery,  I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number
WHERE year = 2021 and month = 7 and day = 28
and atm_location = "Leggett Street" and transaction_type = "withdraw";

--Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista,


--transcript/interview #3
--As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--The thief then asked the person on the other end of the phone to purchase the flight ticket.


--what flight
SELECT name FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = (SELECT id FROM flights WHERE year = 2021 and month = 7 and day = 29 AND
origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour, minute LIMIT 1);
--DORIS, sofia, bruce, edward, kelsey, taylor, kenny, luca

--DUP NAMES: BRUCE and LUCA

--select the name where they were on the phone for less than 60 seconds.
SELECT name FROM people
join phone_calls ON phone_calls.caller = people.phone_number
where year =2021 and month =7 and day = 28 and duration < 60;
--Sofia, Kelsey, Bruce, Kelsey, Taylor, Diana,Carina,Kenny,Benista

--WHAT CITY
SELECT city from airports
where id = (SELECT destination_airport_id FROM flights
WHERE year = 2021 and month = 7 and day = 29
and origin_airport_id = (SELECT id from airports where city = "Fiftyville")
ORDER BY hour, minute LIMIT 1);
    --NEW YORK CITY

--find who he called
SELECT phone_number from people where name = "Bruce";
    --(367) 555-5533

--ACCOMPLIANCE = robin
select name from people
WHERE phone_number =
(SELECT receiver FROM phone_calls WHERE year = 2021 and month = 7 and day = 28 and duration < 60 and caller = "(367) 555-5533");
--ROBIN
