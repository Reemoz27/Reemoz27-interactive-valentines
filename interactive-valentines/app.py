from flask import Flask, render_template, request

app = Flask(__name__)

# Custom messages for each "no" response
no_messages = [
    "WYM NO???",
    "AY DONT PLAY WITH ME RIGHT NOW.",
    "I’m serious bro 👊",
    "I’m just gonna keep getting bigger🤷‍♀️"
]

@app.route("/", methods=["GET"])
def letter():
    # First page
    return render_template(
        "letter.html",
        size=20,          # text size
        img_size=300,     # image width
        message="Dear valentines receiver, will you be my special valentines??",
        image="pic1.jpg",
        step=0            # counter for "no" responses
    )

@app.route("/response", methods=["POST"])
def response():
    user_input = request.form.get("user_input").strip().lower()
    step = int(request.form.get("step", 0))
    size = int(request.form.get("size", 20))
    img_size = int(request.form.get("img_size", 300))

    if user_input == "yes":
        return render_template("yay.html")
    else:
        size += 10        # text grows
        img_size += 20    # image grows

        # Pick message based on step, loop after 4 messages
        message = no_messages[step % len(no_messages)]
        step += 1

        image = "pic2.jpg"  # same image for all "no"

        return render_template(
            "letter.html",
            size=size,
            img_size=img_size,
            message=message,
            image=image,
            step=step
        )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render sets this automatically
    app.run(host="0.0.0.0", port=port) 
