class AIManager {

    static chatInput =
        document.getElementById("chatInput");

    static sendButton =
        document.getElementById("sendMessage");

    static chatMessages =
        document.getElementById("chatMessages");

    static init() {

        this.registerEvents();

    }

    static registerEvents() {

        this.sendButton.addEventListener(
            "click",
            () => this.send()
        );

        this.chatInput.addEventListener(
            "keypress",
            (event) => {

                if (event.key === "Enter") {

                    this.send();

                }

            }
        );

    }

    static async send() {

        const message =
            this.chatInput.value.trim();

        if (!message) {

            return;

        }

        this.addMessage(
            "user",
            message
        );

        this.chatInput.value = "";

        this.sendButton.disabled = true;

        try {

            const response =
                await ApiService.chat(message);

            if (!response) {

                this.addMessage(
                    "assistant",
                    "Something went wrong."
                );

                return;

            }

            this.addMessage(
                "assistant",
                response.reply
            );

        }

        catch (error) {

            console.error(error);

            this.addMessage(
                "assistant",
                "Unable to contact AI service."
            );

        }

        finally {

            this.sendButton.disabled = false;

            this.chatInput.focus();

        }

    }

    static addMessage(sender, text) {

        const div =
            document.createElement("div");

        div.className =
            sender === "user"
                ? "text-end mb-2"
                : "text-start mb-2";

        div.innerHTML = `
            <div class="p-2 rounded border">
                ${text}
            </div>
        `;

        this.chatMessages.appendChild(div);

        this.chatMessages.scrollTop =
            this.chatMessages.scrollHeight;

    }

}