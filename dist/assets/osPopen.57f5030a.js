import{e}from"./cmdExec.918aee2e.js";import{g as a,d as l,r as t,k as n,h as d,w as o,l as u,F as s,s as m,o as r,v as c}from"./vendor.cedc5fa0.js";import"./request.0bf35abf.js";import"./index.8fd6f836.js";const f=m("h1",null,"command Execute os.popen",-1),p={style:{display:"flex","justify-content":"flex-end"}},i=c(" 验证 ");var v=a({setup(a){const c=l({cmd:"",code:"ls",name:""}),v=async()=>{await e(c)};return(e,a)=>{const l=t("n-input"),_=t("n-form-item"),b=t("n-button"),x=t("n-col"),y=t("n-row"),h=t("n-form");return r(),n(s,null,[f,d(h,{model:u(c),ref:(e,a)=>{a.formRef=e}},{default:o((()=>[d(_,{path:"cmd",label:"cmd"},{default:o((()=>[d(l,{value:u(c).cmd,"onUpdate:value":a[0]||(a[0]=e=>u(c).cmd=e)},null,8,["value"])])),_:1}),d(_,{path:"code",label:"code"},{default:o((()=>[d(l,{value:u(c).code,"onUpdate:value":a[1]||(a[1]=e=>u(c).code=e)},null,8,["value"])])),_:1}),d(_,{path:"name",label:"name"},{default:o((()=>[d(l,{value:u(c).name,"onUpdate:value":a[2]||(a[2]=e=>u(c).name=e)},null,8,["value"])])),_:1}),d(y,{gutter:[0,24]},{default:o((()=>[d(x,{span:24},{default:o((()=>[m("div",p,[d(b,{onClick:v,round:"",type:"primary"},{default:o((()=>[i])),_:1})])])),_:1})])),_:1})])),_:1},8,["model"])],64)}}});export{v as default};
