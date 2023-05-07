#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17G65)
# Created On  : Python 3.7.0
# Created By  : Jeromie Kirchoff
# Created Date: Mon Aug 02 17:46:00 PDT 2018
# =============================================================================
# Answer for: https://stackoverflow.com/q/10147455/1896134
# =============================================================================
"""The Module Has Been Build for Sending Emails from your Gmail Account.
This is a full working example, just fill out the variables and
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
YOU MUST CREATE AND USE AN APP PASSWORD!!!!
https://support.google.com/accounts/answer/185833?hl=en
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
Otherwise when you run
jkirchoff$ python3 sendgmail.py
You get the message
Error: (535, b'5.7.8 Username and Password not accepted. Learn more at
5.7.8  https://support.google.com/mail/?p=BadCredentials
z90-h3zf2215251alemzk.85 - gsmtp')!
But if you have the correct Application password
jkirchoff$ python3 sendgmail.py
Email sent!
"""
import smtplib
def send_forget_password_mail(email,token):
    # =============================================================================
    # Imports
    # =============================================================================
    

    # =============================================================================
    # SET EMAIL LOGIN REQUIREMENTS
    # =============================================================================
    
    sent_from = 'themikey@themikey.ir'

    # =============================================================================
    # SET THE INFO ABOUT THE SAID EMAIL
    # =============================================================================
    recipient_list = [email,]
    subject = "Your forget password link"
    message = (f"Hi,\n you requested for reset password, if you didn't request just ignore this email.\nhttps://themikey.ir/reset-password/{token}/")

    # email_text = """\
    # From: %s
    # To: %s
    # Subject: %s

    # %s
    # """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

    # =============================================================================
    # SEND EMAIL OR DIE TRYING!!!
    # Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
    # =============================================================================
    from django.core.mail import send_mail
    # try:
    send_mail(
        subject,
        message,
        sent_from,
        recipient_list,
        fail_silently=False,
    )
    #     print('Email sent!')
    # except Exception as exception:
    #     print("Error: %s!\n\n" % exception)