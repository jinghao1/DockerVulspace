import{p as e}from"./sqlInjection.acb772ca.js";import{g as a,d as l,r as n,k as t,h as u,w as s,l as o,F as d,s as p,o as r,v as f}from"./vendor.cedc5fa0.js";import"./request.027d6cf7.js";import"./index.6f530c9a.js";const i=p("h1",null,"pysql execute",-1),m={style:{display:"flex","justify-content":"flex-end"}},v=f(" 验证 ");var c=a({setup(a){const f=l({id:"",name:"",phone1:"",sql:"song"}),c=async()=>{await e(f)};return(e,a)=>{const l=n("n-input"),h=n("n-form-item"),q=n("n-button"),_=n("n-col"),y=n("n-row"),b=n("n-form");return r(),t(d,null,[i,u(b,{model:o(f),ref:(e,a)=>{a.formRef=e}},{default:s((()=>[u(h,{path:"id",label:"id"},{default:s((()=>[u(l,{value:o(f).id,"onUpdate:value":a[0]||(a[0]=e=>o(f).id=e)},null,8,["value"])])),_:1}),u(h,{path:"name",label:"name"},{default:s((()=>[u(l,{value:o(f).name,"onUpdate:value":a[1]||(a[1]=e=>o(f).name=e)},null,8,["value"])])),_:1}),u(h,{path:"phone1",label:"phone1"},{default:s((()=>[u(l,{value:o(f).phone1,"onUpdate:value":a[2]||(a[2]=e=>o(f).phone1=e)},null,8,["value"])])),_:1}),u(h,{path:"sql",label:"sql"},{default:s((()=>[u(l,{value:o(f).sql,"onUpdate:value":a[3]||(a[3]=e=>o(f).sql=e)},null,8,["value"])])),_:1}),u(y,{gutter:[0,24]},{default:s((()=>[u(_,{span:24},{default:s((()=>[p("div",m,[u(q,{onClick:c,round:"",type:"primary"},{default:s((()=>[v])),_:1})])])),_:1})])),_:1})])),_:1},8,["model"])],64)}}});export{c as default};
