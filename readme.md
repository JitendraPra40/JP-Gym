# JP Gym Management System

The JP Gym Management System is a web-based application built using Django that helps gym owners manage their daily operations. It includes features such as member enrollment, workout attendance tracking, trainer assignments, and more. The system allows gym members to register, select membership plans, track attendance, and interact with trainers. Admins can manage all gym data via an intuitive admin panel.

## Features

### 1. **User Authentication**
   - Users can sign up, log in, and log out.
   - Passwords are securely handled using Django's built-in authentication system.
   - Admins and gym members have different access levels.

### 2. **Profile Management**
   - Users can view and update their profile information.
   - Members can track their enrollment details, payment status, trainer details, and attendance history.

### 3. **Membership Plans**
   - Gym members can choose from various membership plans offered by the gym.
   - Plans include information about pricing and validity.
   - Members can select a plan during enrollment.

### 4. **Trainer Management**
   - Admins can add, update, or remove trainer details.
   - Each trainer's name, contact information, salary, and assigned gym sessions are tracked.
   - Members can select trainers when enrolling.

### 5. **Gallery**
   - Gym's photos and other media can be displayed in a gallery for potential members to view.
   - Admins can add and manage images.

### 6. **Attendance Tracking**
   - Members can log their workout attendance.
   - Trainers can track members' login and logout times, as well as workout details.
   - Admins can monitor attendance patterns.

### 7. **Contact Form**
   - Users can contact the gym for inquiries or support via a contact form.
   - Admins will be notified of new inquiries.

### 8. **Reviews**
   - Users can submit reviews about their experience at the gym.
   - Feedback helps improve services and provides insights into member satisfaction.

### 9. **Admin Panel**
   - Admins can manage all aspects of the gym, including members, trainers, attendance, gallery, and more.
   - The Django admin interface provides an easy-to-use backend for managing data.

## Installation Guide

To get started with the JP Gym Management System, follow the steps below to set it up on your local machine.

### Prerequisites

Make sure you have the following software installed on your local machine:

- **Python 3.x**: The programming language used for the project.
- **Django**: A high-level Python web framework.
- **MySQL** (or other supported databases): The database used to store application data.
- **Git**: Version control tool to clone the repository.

### Step 1: Clone the Repository

To clone the repository to your local machine, use Git:

```bash
git clone https://github.com/your-username/jp-gym.git
cd jp-gym
