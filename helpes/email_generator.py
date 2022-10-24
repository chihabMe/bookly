
from typing import Dict


def email_generator(from_,to,subject,text,html)->Dict:
    return {
      'Messages': [
    {
      "From": {
        "Email": from_.get("email"),
        "Name":from_.get("name") 
      },
      "To": [
        {
          "Email": to.get("email"),
          "Name": to.get("name") 
        }
      ],
      "Subject": subject,
      "TextPart": text,
      "HTMLPart": html,
    }
  ]
  }
    










