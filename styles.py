# styles.py

BUTTON_THEME = """
/* -----------------------------------------------------------------------
   1. PRIMARY ACTION BUTTONS (Login, Register, Save, Confirm)
   Look: Solid Indigo/Purple color, white text, rounded
----------------------------------------------------------------------- */
QPushButton#pushButton_2,    /* Login Button */
QPushButton#pushButton_9,    /* Login (Register pg) */
QPushButton#pushButton_10,   /* Register / Save Profile */
QPushButton#saveappointment, /* Save Appt */
QPushButton#confirm_btn,     /* Confirm Action */
QPushButton#complete_btn,    /* Complete Action */
QPushButton#update_btn,      /* Update Action */
QPushButton#update_appointment_btn, 
QPushButton#pushButton_7     /* Send Contact Form */
{
    background-color: #4F46E5; /* Indigo */
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: bold;
    border: none;
}

QPushButton#pushButton_2:hover, 
QPushButton#pushButton_9:hover, 
QPushButton#pushButton_10:hover, 
QPushButton#saveappointment:hover,
QPushButton#confirm_btn:hover,
QPushButton#complete_btn:hover {
    background-color: #4338CA; /* Darker Indigo */
}

QPushButton#pushButton_2:pressed {
    background-color: #312E81;
}

/* -----------------------------------------------------------------------
   2. DANGER BUTTONS (Logout, Cancel, No Show)
   Look: Light Red background, Red text
----------------------------------------------------------------------- */
QPushButton[text="Log Out"], 
QPushButton[text="Cancel"], 
QPushButton#noshow_btn,
QPushButton#cancel_btn,
QPushButton#cancel_patient_appointment_btn,
QPushButton#pushButton_12, /* Logout Sidebar */
QPushButton#pushButton_14, /* Logout Sidebar */
QPushButton#pushButton_17, /* Logout Sidebar */
QPushButton#pushButton_28  /* Logout Sidebar */
{
    background-color: #FEF2F2; /* Very Light Red */
    color: #DC2626;            /* Red Text */
    border: 1px solid #FECACA;
    border-radius: 8px;
    padding: 6px 12px;
    font-weight: 600;
}

QPushButton[text="Log Out"]:hover, 
QPushButton#noshow_btn:hover,
QPushButton#cancel_btn:hover {
    background-color: #FEE2E2; /* Slightly darker red on hover */
    border-color: #FCA5A5;
}

/* -----------------------------------------------------------------------
   3. SIDEBAR / NAVIGATION BUTTONS
   Look: Transparent background, turns Grey on hover
----------------------------------------------------------------------- */
QPushButton#pushButton_3, QPushButton#pushButton_4, QPushButton#pushButton_5,
QPushButton#pushButton_6, QPushButton#pushButton_8,
QPushButton#pushButton_11, QPushButton#pushButton_13,
QPushButton#pushButton_15, QPushButton#pushButton_16,
QPushButton#pushButton_18, QPushButton#pushButton_19,
QPushButton#pushButton_21, QPushButton#pushButton_22, QPushButton#pushButton_23,
QPushButton#pushButton_27, QPushButton#pushButton_29,
QPushButton#pushButton_30, QPushButton#pushButton_31 
{
    background-color: transparent;
    color: black;
    text-align: left;
    padding-left: 20px;
    border-radius: 10px;
    border: none;
    font-size: 14px;
}

QPushButton#pushButton_3:hover, 
QPushButton#pushButton_11:hover, 
QPushButton#pushButton_21:hover {
    background-color: #E5E7EB; /* Light Grey Hover */
}

QPushButton#pushButton_3:checked, 
QPushButton#pushButton_11:checked, 
QPushButton#pushButton_21:checked {
    background-color: #D1D5DB; /* Active State Grey */
    font-weight: bold;
}

/* -----------------------------------------------------------------------
   4. HEADER LINKS (Home, About Us, Contact Us)
----------------------------------------------------------------------- */
QPushButton#pushButton_4, QPushButton#pushButton_5, QPushButton#pushButton_6 {
    color: white;
    font-weight: bold;
    background-color: transparent;
}
QPushButton#pushButton_4:hover, QPushButton#pushButton_5:hover, QPushButton#pushButton_6:hover {
    color: #E0E7FF; /* Light blue text on hover */
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
}

/* -----------------------------------------------------------------------
   5. STANDARD INPUTS (Optional - just makes them cleaner)
----------------------------------------------------------------------- */
QLineEdit, QDateEdit, QTimeEdit {
    border: 1px solid #D1D5DB;
    border-radius: 6px;
    padding: 5px;
    background-color: white;
}
QLineEdit:focus {
    border: 2px solid #4F46E5;
}
"""