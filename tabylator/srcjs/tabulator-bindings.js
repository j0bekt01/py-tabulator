(()=>{var o=class extends Shiny.OutputBinding{find(n){return n.find(".shiny-tabulator-output")}renderValue(n,e){console.log("payload",e);let u=e.schema.fields.map(t=>({title:t.name,field:t.name,hozAlign:["integer","number"].includes(t.type)?"right":"left",editor:!0}));new Tabulator(n,{data:e.data,layout:"fitColumns",columns:u}).on("rowClick",function(t,a){let i=`${n.id}_row`;console.log(i,a.getData()),Shiny.onInputChange(i,a.getData())})}};Shiny.outputBindings.register(new o,"shiny-tabulator-output");})();
