<template>
    <v-tabs>
        <v-tab >

               <span v-for="(t,k) in map_data"
                    :key="k"

               >
                   <span class="Route" v-bind:class="{'Green':(t.transport==='metro'),                                        //tram
                                                       'LightBlue':(t.transport==='bus'),                 //bus
                                                       'Pink':(t.transport==='tram'),            //trolley
                                                       'Orange':(t.transport==='trolley')
                                                        }">
                       <span v-if="t.transport!=='walk'">
                           {{t.route}}
                       </span>
                       <span v-else>
                             <i class="fas fa-walking fa-2x" style="color: darkslategray;line-height: 12px"/>
                       </span>

                   </span>
                   <span v-if="k!==(map_data.length-1)" class="m-1" style="color: black;">
                        >
                   </span>
               </span>
                <label style="font-size: small"  class="ml-6 text-lowercase">, 2hr 30min</label>
        </v-tab>
        <v-tab-item>
            <v-container fluid lazy >
                <v-row   dense style="height: auto"  >
                    <v-col md="4" >
                        <SearchRouteDirectionTimeline v-bind:timeline_data="map_data"/>
                    </v-col>
                    <v-col md="8">
                        <SearchRoutesDirectionMap  v-bind:map_data="map_data"/>
                    </v-col>
                </v-row>
            </v-container>
        </v-tab-item>


    </v-tabs>

</template>

<script>
    import SearchRouteDirectionTimeline from "./SearchRoutesDirectionTimeline";
    import SearchRoutesDirectionMap from "./SearchRoutesDirectionMap";


     class Map_Line{
        coordinates=[];
        places=[];
        accessibility=[];
        transport="";
        route="";
        show=false;

    }



    export default {
        name: "SearchRoutesDirections",
        components: {SearchRoutesDirectionMap, SearchRouteDirectionTimeline},
        data: () =>({
            points:[
                {coordinates:[37.942907, 23.740806],name:"place 1",transport:"bus",route:"203",accessibility:true},
                {coordinates:[37.943408, 23.740619],name:"place 2",transport:"bus",route:"203",accessibility:true},
                {coordinates:[37.948010, 23.739489],name:"place 3",transport:"bus",route:"203",accessibility:true},
                {coordinates:[37.948010, 23.739489],name:"place 3",transport:"bus",route:"212",accessibility:true},
                {coordinates:[37.961818, 23.736181],name:"place 4",transport:"bus",route:"212",accessibility:false},
                {coordinates:[37.961818, 23.736181],name:"place 4",transport:"trolley",route:"11",accessibility:false},
                {coordinates:[37.983604, 23.730130],name:"place 5",transport:"trolley",route:"11",accessibility:true},
                {coordinates:[37.983604, 23.730130],name:"place 5",transport:"walk",route:"",accessibility:true},
                {coordinates:[37.988610, 23.710346],name:"place 6",transport:"walk",route:"",accessibility:true},
                {coordinates:[37.988610, 23.710346],name:"place 7",transport:"tram",route:"T1",accessibility:true},
                {coordinates:[38.024167, 23.691184],name:"place 8",transport:"tram",route:"T1",accessibility:true},
            ],
            map_data:[],
          }),

        created() {
            let p,next_route;


            this.map_data=[];


            let md=new Map_Line();


            let cur_route=this.points[0].route;
            md.route=cur_route;
            md.transport=this.points[0].transport;



            for (p of this.points){

                next_route=p.route;
                if(next_route !== cur_route){
                    this.map_data.push(md);


                    md=new Map_Line();

                    md.coordinates=[p.coordinates];
                    md.places=[p.name];
                    md.accessibility=[p.accessibility];

                    md.route=next_route;
                    md.transport=p.transport;
                    cur_route=next_route;

                }
                else{
                    md.accessibility.push(p.accessibility);
                    md.coordinates.push(p.coordinates);
                    md.places.push(p.name);

                }

            }
            this.map_data.push(md);


        }


    }
</script>

<style scoped>


    .Green{
        background-color: #006C4A;
    }

    .Gray{
        background-color: #9E9E9E;
    }

    .Pink {
        background-color: #DD137B;
    }

    .LightBlue{
        background-color: #009EC7;
    }

    .Orange{
        background-color: #F27D00;
    }

    .Route{
        color: whitesmoke;
        border-radius: 7px;
        padding: 5px;
        display: inline-block;
    }

</style>