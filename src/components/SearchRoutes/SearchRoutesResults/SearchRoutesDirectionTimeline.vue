<template>
    <v-card color="#FAFAFA" elevation="0">
        <v-timeline
                v-for="(direction,i) in directions"
                :key="i"
                dense
                v-bind:class="{'myClassGreen':(direction.transport==='#DD137B'),                                        //tram
                                                       'myClassPink':(direction.transport==='#009EC7'),                 //bus
                                                       'myClassLightBlue':(direction.transport==='#F27D00'),            //trolley
                                                       }"
                >
                <v-timeline-item fill-dot   :color="direction.transport" class="pb-0 pt-0 ">
                  <v-btn  small  v-on:click="new ShowStations(i)" >

                        Take {{direction.name}} from {{direction.from}} to {{direction.to}}
                  </v-btn>
                </v-timeline-item>
                <div v-if="direction.show_stations">
                    <v-timeline dense    v-bind:class="{'myClassGreen':(direction.transport==='#006C4A'),           //metro
                                                       'myClassPink':(direction.transport==='#DD137B'),             //tram
                                                       'myClassLightBlue':(direction.transport==='#009EC7'),        //bus ////trolley
                                                       'myClassOrange':(direction.transport==='#F27D00')}" class="p-0" >


                        <v-timeline-item class="pb-1" hide-dot

                                         v-for="k in direction.stops"
                                         v-bind:key="k"
                                         :color="direction.transport">
                            Stop {{k}}

                        </v-timeline-item>

                    </v-timeline>

                </div>

        </v-timeline>
    </v-card>
</template>

<script>
    export default {
        name: "SearchRouteDirectionTimeline",
        data: () =>({
            directions:[
                {transport:"#006C4A",name:"1",from:"ok",to:"lol",stops:5,show_stations:false},      //
                {transport:"#DD137B",name:"2",from:"ok2",to:"lol2",stops:7,show_stations:false},
                {transport:"#009EC7",name:"3",from:"ok3",to:"lol3",stops:9,show_stations:false},
                {transport:"#F27D00",name:"4",from:"ok4",to:"lol4",stops:9,show_stations:false}
            ],

        }),
        props:['points'],

        methods:{
            ShowStations(key){
               this.directions[key].show_stations=!this.directions[key].show_stations;

            }
        }
    }
</script>

<style >


    .myClassGreen.theme--light.v-timeline:before {
            background: #006C4A;
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