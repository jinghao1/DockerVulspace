import{b as e}from"./sqlInjection.13fa7b87.js";import{g as a,d as l,r as n,k as t,h as u,w as s,l as o,F as d,p,o as r,q as f}from"./vendor.4a6a7557.js";import"./request.ceb0393e.js";const m=p("h1",null,"sql insert mysql.executemany",-1),i={style:{display:"flex","justify-content":"flex-end"}},v=f(" 验证 ");var h=a({setup(a){const f=l({id:"",name:"song",phone1:"13322443212",sql:""}),h=async()=>{await e(f)};return(e,a)=>{const l=n("n-input"),c=n("n-form-item"),q=n("n-button"),b=n("n-col"),y=n("n-row"),_=n("n-form");return r(),t(d,null,[m,u(_,{model:o(f),ref:(e,a)=>{a.formRef=e}},{default:s((()=>[u(c,{path:"id",label:"id"},{default:s((()=>[u(l,{value:o(f).id,"onUpdate:value":a[0]||(a[0]=e=>o(f).id=e)},null,8,["value"])])),_:1}),u(c,{path:"name",label:"name"},{default:s((()=>[u(l,{value:o(f).name,"onUpdate:value":a[1]||(a[1]=e=>o(f).name=e)},null,8,["value"])])),_:1}),u(c,{path:"phone1",label:"phone1"},{default:s((()=>[u(l,{value:o(f).phone1,"onUpdate:value":a[2]||(a[2]=e=>o(f).phone1=e)},null,8,["value"])])),_:1}),u(c,{path:"sql",label:"sql"},{default:s((()=>[u(l,{value:o(f).sql,"onUpdate:value":a[3]||(a[3]=e=>o(f).sql=e)},null,8,["value"])])),_:1}),u(y,{gutter:[0,24]},{default:s((()=>[u(b,{span:24},{default:s((()=>[p("div",i,[u(q,{onClick:h,round:"",type:"primary"},{default:s((()=>[v])),_:1})])])),_:1})])),_:1})])),_:1},8,["model"])],64)}}});export{h as default};
