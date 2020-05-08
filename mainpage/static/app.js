////check in static where 2nd folder
//new Vue({
// el: '#main_app',
// data: {
// orders:[]
// },
// created: function () {
// const vm = this;
// axios.get('/vue/')
// .then(function(response){
// vm.orders=response.data
// })
// }
//
//}
//
//)
var app = new Vue({
el: '#app',
data:{
showHome: null,
showCheck: null,
showCoin: false,
showUser: false,
userProfilePic: 'https://sun1.tele2-kz-almaty.userapi.com/Syp1kcyrf8yQ_byZ0Jqf..',
effect: 'lni-tada-effect'
},
methods:{
getIm () {
this.menu = 'http://127.0.0.1:8000/contact/'
this.login ='http://127.0.0.1:8000/api/login/?next=/'

}


}
})
