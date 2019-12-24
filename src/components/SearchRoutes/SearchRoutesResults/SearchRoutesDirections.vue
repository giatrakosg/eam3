<template>
    <v-tabs>
        <v-tab >

                Route option 1

        </v-tab>
        <v-tab-item>
            <v-container fluid lazy >
                <v-row   dense style="height: auto"  >
                    <v-col md="4" >
                        <SearchRouteDirectionTimeline/>
                    </v-col>
                    <v-col md="8">
                        <SearchRoutesDirectionMap  v-bind:map_data="this.map_data"/>
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
        transport="";

    }

    export default {
        name: "SearchRoutesDirections",
        components: {SearchRoutesDirectionMap, SearchRouteDirectionTimeline},
        data: () =>({
            points:[
                {coordinates:[37.942907, 23.740806],name:"place 1",transport:"bus",route:"203"},
                {coordinates:[37.943408, 23.740619],name:"place 2",transport:"bus",route:"203"},
                {coordinates:[37.948010, 23.739489],name:"place 3",transport:"bus",route:"203"},
                {coordinates:[37.948010, 23.739489],name:"place 3",transport:"walk",route:""},
                {coordinates:[37.961818, 23.736181],name:"place 4",transport:"walk",route:""},
                {coordinates:[37.961818, 23.736181],name:"place 4",transport:"trolley",route:"11"},
                {coordinates:[37.983604, 23.730130],name:"place 5",transport:"trolley",route:"11"},
                {coordinates:[37.983604, 23.730130],name:"place 5",transport:"walk",route:""},
                {coordinates:[37.988610, 23.710346],name:"place 6",transport:"walk",route:""},
                {coordinates:[37.988610, 23.710346],name:"place 6",transport:"metro",route:"M1"},
                {coordinates:[37.988610, 23.710346],name:"place 7",transport:"tram",route:"M1"},
                {coordinates:[38.024167, 23.691184],name:"place 8",transport:"tram",route:"T1"},
            ],
            map_data:[],
            timeline_data:[],




        }),

        created() {
            let p,next_tr;


            this.map_data=new Array(Map_Line);
            let md=new Map_Line();

            let cur_tr=this.points[0].transport;
            md.transport=cur_tr;


            for (p of this.points){
                next_tr=p.transport;
                if(next_tr !== cur_tr){
                    this.map_data.push(md);
                    md=new Map_Line();
                    md.coordinates=[p.coordinates];
                    md.transport=next_tr;
                    cur_tr=next_tr;

                }
                else{
                    md.coordinates.push(p.coordinates);

                }

            }
            this.map_data.push(md);


        }


    }
</script>

<style scoped>

</style>