-- ===================================
-- Property Mamangement Booking System
-- ===================================

CREATE DATABASE property_management;

USE property_management;

-- Creating table to store the 6 rooms 
CREATE TABLE rooms (
    room_id INT PRIMARY KEY,
    room_number INT NOT NULL,
    price_per_night DECIMAL(10,2) NOT NULL
);

-- Storing guest information to connect to booking information later on 
CREATE TABLE guests (
    guest_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_name VARCHAR(100) NOT NULL,
    number_of_guests INT NOT NULL
);

-- Link each booking to an existing guest and room
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,

    FOREIGN KEY (guest_id) REFERENCES guests(guest_id), -- Foreign keys maintain relationships between tables, guests and rooms
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);
-- ===============
-- Testing section 
-- ===============

 -- Creating 6 rooms and setting a fixed price temporarily
INSERT INTO rooms (room_id, room_number, price_per_night)
VALUES
(1, 1, 100.00),
(2, 2, 100.00),
(3, 3, 100.00),
(4, 4, 100.00),
(5, 5, 100.00),
(6, 6, 100.00);

-- Testing with test guest Sarah
INSERT INTO guests (guest_name, number_of_guests)
VALUES ('Sarah', 2);

-- Assigning Sarah a room, check in and check out dates 
SELECT * FROM guests;
INSERT INTO bookings (guest_id, room_id, check_in, check_out)
VALUES (1, 3, '2026-11-10', '2026-11-13');

-- Combining the bookings, rooms and guests using their IDS
-- Displaying the guest name instead of their ID 
SELECT
    bookings.booking_id,
    guests.guest_name,
    rooms.room_number,
    bookings.check_in,
    bookings.check_out
FROM bookings
JOIN guests
    ON bookings.guest_id = guests.guest_id
JOIN rooms
    ON bookings.room_id = rooms.room_id;
    
-- Availability tests 
SELECT *
FROM bookings
WHERE room_id = 3
AND check_in < '2026-11-15'
AND check_out > '2026-11-11';

SELECT *
FROM bookings
WHERE room_id = 3
AND check_in < '2026-11-16'
AND check_out > '2026-11-13';