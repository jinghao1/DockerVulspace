import{c as e}from"./sqlInjection.b95d3d3a.js";import{g as a,d as l,r as t,k as n,h as u,w as s,l as o,F as d,s as p,o as r,v as f}from"./vendor.cedc5fa0.js";import"./request.0bf35abf.js";import"./index.8fd6f836.js";const i=p("h1",null,"sqlite3 executescript update",-1),m={style:{display:"flex","justify-content":"flex-end"}},v=f(" 验证 ");var c=a({setup(a){const f=l({id:"",name:"song",phone1:"15523421232",sql:""}),c=async()=>{await e(f)};return(e,a)=>{const l=t("n-input"),h=t("n-form-item"),b=t("n-button"),q=t("n-col"),_=t("n-row"),j=t("n-form");return r(),n(d,null,[i,u(j,{model:o(f),ref:(e,a)=>{a.formRef=e}},{default:s((()=>[u(h,{path:"id",label:"id"},{default:s((()=>[u(l,{value:o(f).id,"onUpdate:value":a[0]||(a[0]=e=>o(f).id=e)},null,8,["value"])])),_:1}),u(h,{path:"name",label:"name"},{default:s((()=>[u(l,{value:o(f).name,"onUpdate:value":a[1]||(a[1]=e=>o(f).name=e)},null,8,["value"])])),_:1}),u(h,{path:"phone1",label:"phone1"},{default:s((()=>[u(l,{value:o(f).phone1,"onUpdate:value":a[2]||(a[2]=e=>o(f).phone1=e)},null,8,["value"])])),_:1}),u(h,{path:"sql",label:"sql"},{default:s((()=>[u(l,{value:o(f).sql,"onUpdate:value":a[3]||(a[3]=e=>o(f).sql=e)},null,8,["value"])])),_:1}),u(_,{gutter:[0,24]},{default:s((()=>[u(q,{span:24},{default:s((()=>[p("div",m,[u(b,{onClick:c,round:"",type:"primary"},{default:s((()=>[v])),_:1})])])),_:1})])),_:1})])),_:1},8,["model"])],64)}}});export{c as default};
