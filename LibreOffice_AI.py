from baichat_py import BAIChat

def buat_konten():
    chat = BAIChat()
    doc = XSCRIPTCONTEXT.getDocument()
    selection = doc.getCurrentSelection()
    if selection.supportsService("com.sun.star.text.TextRanges"):
        for textRange in selection:
            prompt = textRange.getString()
            response_text = chat.sync_ask(prompt).text
            
            cursor = doc.getCurrentController().getViewCursor()
            docText = doc.Text
            
            # Set Selected Text as Title
            text = textRange.getString()
            text_with_newline = text + "\n"
            textRange.setString(text_with_newline)
            
            # insert BAIChat response to current document
            docText.insertString(cursor, response_text, False)
            
            # Apply styling
            textCursor = textRange.getText().createTextCursorByRange(textRange)
            textCursor.setPropertyValue("CharWeight", 150) # set title bold
    else:
        return "Invalid selection"