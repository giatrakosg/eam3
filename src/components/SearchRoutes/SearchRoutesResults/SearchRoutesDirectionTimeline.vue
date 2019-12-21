<template>
    <v-card color="#FAFAFA" elevation="0">
        <v-timeline
                v-for="(direction,i) in directions"
                :key="i"
                dense
                class="pl-0">
                <v-timeline-item  :color="direction.transport" class="pb-1">
                  <v-btn  small  v-on:click="ShowStations(i)" >

                        Take {{direction.name}} from {{direction.from}} to {{direction.to}}
                  </v-btn>
                </v-timeline-item>
                <div v-if="direction.show_stations">
                    <v-timeline-item small class="pb-1"

                                     v-for="k in direction.stops"
                                     v-bind:key="k"
                                     :color="direction.transport">
                        Stop {{k}}

                    </v-timeline-item>
                </div>

        </v-timeline>
    </v-card>
</template>

<script>
    export default {
        name: "SearchRouteDirectionTimeline",
        data: () =>({
            directions:[
                {transport:"#006C4A",name:"1",from:"ok",to:"lol",stops:5,show_stations:false},
                {transport:"#DD137B",name:"2",from:"ok2",to:"lol2",stops:7,show_stations:false},
                {transport:"#009EC7",name:"3",from:"ok3",to:"lol3",stops:9,show_stations:false},
                {transport:"#F27D00",name:"4",from:"ok4",to:"lol4",stops:9,show_stations:false}
            ],



        }),
        methods:{
            ShowStations(key){
               this.directions[key].show_stations=!this.directions[key].show_stations;

            }
        }
    }
</script>

<style scoped>

</style>