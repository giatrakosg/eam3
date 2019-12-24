<template >


    <l-map  style="height: 600px;z-index: 0" :zoom="zoom" :center="center">
        <l-tile-layer
                :url="url"
        />
        <l-polyline
                v-for="(line,i) in m_data"
                :key="i"
                :lat-lngs="line.coordinates"
                :color="getColor(i)"
                :dash-array="getDash(i)"
                :weight="5"
        >

        </l-polyline>


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
                circle: {
                    center:[38.024167, 23.691184],
                    radius: 6,
                    color: 'red'
                },


                m_data: this.map_data

            };
        },
        props:['map_data'],
        methods:{
            getColor(i){
                switch (this.map_data[i].transport) {
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
            getDash(i){
                switch (this.map_data[i].transport) {
                    case "walk":
                        return 7;
                    default:
                        return 0;

                }
            }
        }



    }


</script>

<style scoped>



</style>