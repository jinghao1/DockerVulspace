import{u as a}from"./csrf.d70e8a13.js";import{g as e,d as l,r as s,k as t,h as r,w as u,l as n,F as o,s as f,o as d,v as i}from"./vendor.cedc5fa0.js";import"./request.5c5bc3d8.js";import"./index.fa2420f2.js";const p=f("h1",null,"urllib_ssrf",-1),c={style:{display:"flex","justify-content":"flex-end"}},m=i(" 验证 ");var v=e({setup(e){const i=l({url:"file:///etc/passwd"}),v=async()=>{await a(i)};return(a,e)=>{const l=s("n-input"),y=s("n-form-item"),_=s("n-button"),j=s("n-col"),b=s("n-row"),w=s("n-form");return d(),t(o,null,[p,r(w,{model:n(i),ref:(a,e)=>{e.formRef=a}},{default:u((()=>[r(y,{path:"url",label:"url"},{default:u((()=>[r(l,{value:n(i).url,"onUpdate:value":e[0]||(e[0]=a=>n(i).url=a)},null,8,["value"])])),_:1}),r(b,{gutter:[0,24]},{default:u((()=>[r(j,{span:24},{default:u((()=>[f("div",c,[r(_,{onClick:v,round:"",type:"primary"},{default:u((()=>[m])),_:1})])])),_:1})])),_:1})])),_:1},8,["model"])],64)}}});export{v as default};
