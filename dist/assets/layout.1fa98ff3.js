import{g as a}from"./index.71d33363.js";import{g as l,o as e,c as n,h as s,i as o,u as t,j as r,r as i,k as u,w as d,l as c,m as p,N as v,p as h}from"./vendor.4a6a7557.js";const w={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},m=s("path",{d:"M352 48H160a48 48 0 0 0-48 48v368l144-128l144 128V96a48 48 0 0 0-48-48z",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1);var x=l({name:"BookmarkOutline",render:function(a,l){return e(),n("svg",w,[m])}});const f={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},g=s("path",{d:"M98 190.06l139.78 163.12a24 24 0 0 0 36.44 0L414 190.06c13.34-15.57 2.28-39.62-18.22-39.62h-279.6c-20.5 0-31.56 24.05-18.18 39.62z",fill:"currentColor"},null,-1);var k=l({name:"CaretDownOutline",render:function(a,l){return e(),n("svg",f,[g])}});const j={class:"menu"};var y=l({setup(l){const n=o(!1),h=a(),w=t(),m=r(),f=o(w.name),g=a=>{f.value=a,m.push({name:a})},y=a=>a.label,b=a=>p(v,null,{default:()=>p(x)}),z=()=>p(v,null,{default:()=>p(k)});return(a,l)=>{const o=i("n-menu"),t=i("n-layout-sider");return e(),u("div",j,[s(t,{bordered:"","collapse-mode":"width","collapsed-width":64,width:240,collapsed:n.value},{default:d((()=>[s(o,{"onUpdate:value":g,collapsed:n.value,"collapsed-width":64,"collapsed-icon-size":22,options:c(h),"render-label":y,"render-icon":b,"expand-icon":z,value:f.value},null,8,["collapsed","options","value"])])),_:1},8,["collapsed"])])}}});const b={class:"huoxian-layout"},z={class:"huoxian-main"},B={class:"huoxian-main-left"},C=h("div",{class:"huoxian-header"},[h("h2",null,"危险函数")],-1),M={class:"huoxian-main-right"},O=h("div",{class:"huoxian-header"},[h("h2",null," 靶场 ")],-1),_={style:{padding:"16px"}};var D=l({setup:a=>(a,l)=>{const n=i("n-layout"),o=i("router-view");return e(),u("div",b,[h("div",z,[h("div",B,[C,s(n,{"has-sider":""},{default:d((()=>[s(y)])),_:1})]),h("div",M,[O,h("div",_,[s(o)])])])])}});export{D as default};
