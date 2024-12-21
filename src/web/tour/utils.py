from django.core.mail import send_mail
from django.utils.timezone import localtime


def send_reservation_email(full_name, recipient_email, tour_title, created_at):
    """
    Sends an email for reservation confirmation.
    Args:
        full_name (str): Full name of the user booking the tour.
        recipient_email (str): Email of the user.
        tour_title (str): The title of the selected tour.
        created_at (datetime): The timestamp when the booking was made.
    """
    # Localize the time (if using timezone-aware datetimes)
    booking_time = localtime(created_at).strftime('%Y-%m-%d %H:%M:%S')

    message = f"""
    Dear {full_name},

    Thank you for choosing our services. We are pleased to confirm your booking for the following tour:

    Tour Title: {tour_title}
    Date and Time of Booking: {booking_time}

    Your reservation has been successfully processed. We look forward to providing you with an exceptional experience. Please feel free to reach out should you require any additional information or assistance prior to your tour.

    We will send you further details and updates closer to the date of your tour.

    If you have any inquiries, do not hesitate to contact us at your convenience.

    Best regards,
    The [Your Tour Company] Team
    """

    send_mail(
        subject='Reservation Confirmation',
        message=message,
        from_email='noreply@yourdomain.com',
        recipient_list=[recipient_email],
    )
