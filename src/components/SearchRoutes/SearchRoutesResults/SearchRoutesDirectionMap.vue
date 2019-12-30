<template >


    <l-map  style="height: 600px;z-index: 0" :zoom="zoom" :center="center">
        <l-tile-layer
                :url="url"
        />
        <div  v-for="(line,i) in map_data"
              :key="i"
        >
            <l-polyline

                    :lat-lngs="line.coordinates"
                    :color="getColor(line.transport)"
                    :dash-array="getDash(line.transport)"
                    :weight="5"
            >

            </l-polyline>
            <l-marker
                    v-if="line.transport==='bus'"
                    :lat-lng="line.coordinates[0]"

            >
                <l-icon>

                    <img src="../../../assets/bus.png" style="width: 25px" >
                </l-icon>

            </l-marker>
            <l-marker
                    v-if="line.transport==='metro'"
                    :lat-lng="line.coordinates[0]"
            >

                <l-icon>

                    <img src="../../../assets/metro.png" style="width: 25px" >
                </l-icon>

            </l-marker>
            <l-marker
                    v-if="line.transport==='walk'"
                    :lat-lng="line.coordinates[0]"
            >

                <l-icon>

                    <i class="fas fa-walking fa-2x " style="color: darkslategray"/>
                </l-icon>

            </l-marker>
            <l-marker
                    v-if="line.transport==='tram'"
                    :lat-lng="line.coordinates[0]"
            >

                <l-icon>

                    <img src="../../../assets/tram.png" style="width: 25px" >
                </l-icon>

            </l-marker>
            <l-marker
                    v-if="line.transport==='trolley'"
                    :lat-lng="line.coordinates[0]"
            >

                <l-icon>

                    <img src="../../../assets/trolley.png" style="width: 25px" >
                </l-icon>

            </l-marker>

        </div>

    </l-map>


</template>

<script>

    export default {
        data () {
            return {
                url: 'http://mt.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                zoom: 13,
                componentKey:0,
                center: [37.984888, 23.730851],
                icon_url:'../../../assets/bus.png',

            };
        },
        props:['map_data'],
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
                        return "black";

                }
            },
            getDash(tr){
                switch (tr) {
                    case "walk":
                        return "4";
                    default:
                        return "0";

                }
            }


        }



    }


</script>

<style scoped>



</style>