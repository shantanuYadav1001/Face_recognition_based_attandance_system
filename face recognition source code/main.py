

import enroll,spreadsheet,emailing,recognition
#recognition.load_facial_encodings_and_names_from_memory()

#spreadsheet.mark_all_absent()

#recognition.run_recognition()



name = input("Enter new attendes name: ")
enroll.enroll_via_camera(name)
