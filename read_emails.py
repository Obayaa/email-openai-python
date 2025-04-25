from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

# SEND MESSAGE VIA EMAIL SECTION
params = {
  "to": "doraappiah@axxendcorp.com",
  "sender": "doraappiah2004@gmail.com",
  "subject": "Exciting Partnership Opportunity with Axxend Corp",
  "msg_html": ''' <h3>Hello from Axxend Tech Solutions!</h3><br /> I hope this email finds you well. 
    I'm reaching out because we've developed an innovative solution that has helped companies like yours increase productivity by 35% on average. 
    Our AI-powered platform streamlines workflow automation while reducing operational costs significantly. <br />
    <br />I'd love to schedule a brief 15-minute call next week to discuss how our solution could specifically benefit your team at Axxend Corp. <br />
    <br />Would Tuesday or Thursday afternoon work best for your schedule?<br /><br />Looking forward to connecting!''',
  "msg_plain": '''Hello from Axxend Tech Solutions!\n\nI hope this email finds you well. 
    I'm reaching out because we've developed an innovative solution that has helped companies like yours increase productivity by 35% on average. 
    Our AI-powered platform streamlines workflow automation while reducing operational costs significantly.
    \n\nI'd love to schedule a brief 15-minute call next week to discuss how our solution could specifically benefit your team at Axxend Corp.
    \n\nWould Tuesday or Thursday afternoon work best for your schedule?\n\nLooking forward to connecting!''',
  "signature": True 
}
message = gmail.send_message(**params)



