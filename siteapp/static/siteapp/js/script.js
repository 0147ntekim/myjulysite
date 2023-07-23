'use strict';

const AmagiLoader = {
    __loader: null,
    show: function () {

        if (this.__loader == null) {
            var divContainer = document.createElement('div');
            divContainer.style.position = 'fixed';
            divContainer.style.left = '0';
            divContainer.style.top = '0';
            divContainer.style.width = '100%';
            divContainer.style.height = '100%';
            divContainer.style.zIndex = '9998';
            divContainer.style.backgroundColor = '#fff';

            var div = document.createElement('div');
            div.style.position = 'absolute';
            div.style.left = '50%';
            div.style.top = '50%';
            div.style.zIndex = '9999';
            div.style.height = '64px';
            div.style.width = '64px';
            div.style.margin = '-13px 0 0 -13px';
            div.style.border = '8px solid greenYellow';
            div.style.borderRadius = '60px';
            div.style.borderTop = '8px solid ghostWhite';
            div.animate([
                { transform: 'rotate(0deg)' },
                { transform: 'rotate(360deg)' }
              ], {
                duration: 2000,
                iterations: Infinity
              });
            divContainer.appendChild(div);
            this.__loader = divContainer
            document.body.appendChild(this.__loader);
        }
        this.__loader.style.display="";
    },
    hide: function(){
        if(this.__loader!=null)
        {
            this.__loader.style.display="none";
        }
    }
}

AmagiLoader.show();
setTimeout(() => {
  AmagiLoader.hide();
}, 3000);


// header background reveal
const headerBg = () =>{
  const header = document.querySelector(".js-header");

  window.addEventListener("scroll", function(){
      if(this.scrollY > 0){
          header.classList.add("bg-reveal");
      }else{
          header.classList.remove("bg-reveal");
      }
  })
}
headerBg();

const reveal = () =>{
  // const button = document.querySelector("#movetop");

  window.addEventListener("scroll", function(){
      if(this.scrollY > 200){
          document.querySelector("#movetop").style.display="block"
      }else{
        document.querySelector("#movetop").style.display="none"
      }
  })
}
reveal();

/* Open */
function openNav() {
  document.getElementById("myNav").style.height = "100%";
}

/* Close */
function closeNav() {
  document.getElementById("myNav").style.height = "0%";
}