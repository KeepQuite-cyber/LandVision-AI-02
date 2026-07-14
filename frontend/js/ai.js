class AIManager {
    static chatInput = document.getElementById("chatInput");
    static sendButton = document.getElementById("sendMessage");
    static chatMessages = document.getElementById("chatMessages");
    static init() {
        this.registerEvents();
    }
    static registerEvents() {
        this.sendButton.addEventListener("click",() => this.send());
        this.chatInput.addEventListener( "keypress", (event) => {
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
        this.addMessage( "user", message);
        this.chatInput.value = "";
        this.showLoader();
        this.sendButton.disabled = true;
        try {
            const response =  await ApiService.chat(message);
            if (!response) {
                this.addMessage("assistant", "Something went wrong.");
                return;
            }
            this.hideLoader();
            await this.addMessage("assistant", response.reply);
            this.executeActions(response.actions);
        }
        catch (error) {
            console.error(error);
            this.hideLoader();
            this.addMessage( "assistant","Unable to contact AI service.");
        }
        finally {
            this.sendButton.disabled = false;
            this.chatInput.focus();
        }
    }
    static addMessage(sender, text) {
        const div = document.createElement("div");
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
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    static showLoader(){
        const div = document.createElement('div')
        div.className = "text-start mb-2"
        div.id = 'ai-loader'
        div.innerHTML = `
        <div class="p-2 rounded border bg-light">
            <span class="loader-dot"></span>
            <span class="loader-dot"></span>
            <span class="loader-dot"></span>
        </div>
        `;
        this.chatMessages.appendChild(div);
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    static hideLoader(){
        const loader = document.getElementById('ai-loader')
        if(loader){
            loader.remove();
        }
    }

    static executeActions(actions){
        console.log(actions)
        if(!Array.isArray(actions) || actions.length === 0){
            return;
        }

        actions.forEach(action => {
            switch (action.action){
                case "highlight_plot":
                    MapManager.highlightPlot(
                    action.plot_number
                );
                break;

                case "highlight_multiple":
                    MapManager.highlightMultiple(
                    action.plots
                );
                break;

                default:
                    console.warn("Unknown AI Action" , action.action)
            }
        });
    }
    static async typeMessage(sender, text) {

    const div = document.createElement("div");

    div.className =
        sender === "user"
            ? "text-end mb-2"
            : "text-start mb-2";

    div.innerHTML = `
        <div class="p-2 rounded border"></div>
    `;

    this.chatMessages.appendChild(div);

    const bubble = div.querySelector("div");

    for (let i = 0; i < text.length; i++) {

        bubble.textContent += text[i];

        this.chatMessages.scrollTop =
            this.chatMessages.scrollHeight;

        await new Promise(resolve =>
            setTimeout(resolve, 15)
        );

    }

}
}