def cleanup_text(text_in):
    out = text_in.replace("(", "")
    return out.replace(")", "")


print(cleanup_text("(BE)"))
