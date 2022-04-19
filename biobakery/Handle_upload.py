

def handle_uploaded_file(f):
    print(f)
    with open('/Users/bengels/Desktop/Uploaded_files/' + str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)