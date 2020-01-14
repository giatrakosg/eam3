<template>
    <v-card color="#FAFAFA" elevation="0">
        <v-timeline
                v-for="(t,i) in td"
                :key="i"
                dense
                v-bind:class="{'myClassGreen':(t.transport==='metro'),                                        //tram
                                                       'myClassLightBlue':(t.transport==='bus'),                 //bus
                                                       'myClassPink':(t.transport==='tram'),            //trolley
                                                       'myClassOrange':(t.transport==='trolley'),
                                                       'myClassGray':(t.transport==='walk')}"

                class="pb-5 pt-0">
                <v-timeline-item fill-dot :color="getColor(t.transport)"   class="pb-0">
                    <template v-slot:icon>
                        <img  v-if="t.transport==='bus'" src="../../../assets/bus.png" style="width: 50px">
                        <img  v-if="t.transport==='metro'" src="../../../assets/metro.png" style="width: 50px">
                        <img  v-if="t.transport==='trolley'" src="../../../assets/trolley.png" style="width: 50px">
                        <img  v-if="t.transport==='tram'" src="../../../assets/tram.png" style="width: 50px">
                        <i v-if="t.transport==='walk'" class="fas fa-walking fa-2x" style="color: darkslategray"/>
                    </template>
                  <v-btn  small  v-on:click="t.show=!t.show" >
                      <div style="font-weight: 300">
                        <div v-if="t.transport==='walk'">
                            <span style="font-weight: 900">walk</span>,  {{t.places[0]}} > {{t.places[t.places.length-1]}}

                        </div>
                        <div v-else>
                            <span style="font-weight: 900">{{t.route}}</span>, {{t.places[0]}} > {{t.places[t.places.length-1]}}
                        </div>
                      </div>
                  </v-btn>
                </v-timeline-item>

                <v-timeline dense   v-if="t.show && t.transport!=='walk'"   class="p-0" >

                    <v-timeline-item class="pb-1" hide-dot

                                     v-for="(place,index) in t.places"
                                     v-bind:key="index"
                                     >
                         {{place}}
                        <span v-if="t.accessibility[index]">
                            <i  class="fas fa-wheelchair fa-1x  ml-2 "/>
                        </span>

                    </v-timeline-item>

                </v-timeline>



        </v-timeline>
    </v-card>
</template>

<script>
    export default {
        name: "SearchRouteDirectionTimeline",
        props:['timeline_data'],
        data: function() {
            return{
                td:this.timeline_data,
            }

        },

        methods:{

            getColor(tr){
                switch (tr) {
                    case "metro":
                        return "#006C4A";
                    case "bus":
                        return "#009EC7";
                    case "tram":
                        return "#DD137B";
                    case "trolley":
                        return "#F27D00";
                    case "walk":
                        return "#9E9E9E";
                    default:
                        return "blue";

                }
            },
        }
    }
</script>

<style >


    .myClassGreen.theme--light.v-timeline:before {
            background: #006C4A;
            width: 5px;
    }

    .myClassGray.theme--light.v-timeline:before {
        background: #9E9E9E;
        width: 5px;
    }

    .myClassPink.theme--light.v-timeline:before {
        background: #DD137B;
        width: 5px;
    }

    .myClassLightBlue.theme--light.v-timeline:before {
        background: #009EC7;
        width: 5px;
    }

    .myClassOrange.theme--light.v-timeline:before {
        background: #F27D00;
        width: 5px;
    }



</style>