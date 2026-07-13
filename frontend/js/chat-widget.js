class ChatWidget{
    static init(){
        this.chatButton= document.getElementById("chatToggle");
        this.chatWidget= document.getElementById("chatWidget");
        this.closeButton=document.getElementById("closeChat");
        this.registerEvents();
    }
    static registerEvents(){
        this.chatButton.addEventListener( "click", ()=>{
                this.chatWidget.style.display="flex";
                this.chatButton.style.display="none";
            }
        );
        this.closeButton.addEventListener("click",
            ()=>{
                this.chatWidget.style.display="none";
                this.chatButton.style.display="block";
            }
        );
    }
}