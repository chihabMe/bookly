
export default class requestApi{
    static csrf:string=''

    constructor(){
        requestApi.csrf = requestApi._getCookie('csrftoken')

    }
    static _configGenerator(method:string,body?:string|FormData):RequestInit{
        return {
            method,
            headers:{
                "Content-Type": typeof body==typeof FormData ? "multipart/form-data" :"application/json",
                "X-CSRFToken":this.csrf,
            },
            body
        }
    }
    static async get(url:string){
        const config= requestApi._configGenerator("GET")
        return await fetch(url,config)
    }
    static async post(url,body:string|FormData){
        const config= requestApi._configGenerator("POST",body)
        return await fetch(url,config)
    }
    static async update(url,body:string|FormData){
        const config= requestApi._configGenerator("PUT",body)
        return await fetch(url,config)
    }
    static async delete(url,body:string|FormData){
        const config= requestApi._configGenerator("DELETE",body)
        return await fetch(url,config)
    }
    static _getCookie(name:string):string {
        let cookieValue:string = "";
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    
    }
}