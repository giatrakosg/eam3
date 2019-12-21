<template >

        <l-map  style="height: 600px;z-index: 0" :zoom="zoom" :center="center">
            <l-tile-layer
                    :url="url"
            />
            <l-polyline
                    :lat-lngs="polyline.latlngs"
                    :color="polyline.color"
                    >
            </l-polyline>

        </l-map>



</template>

<script>

    export default {
        data () {
            return {
                url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
                zoom: 10,
                componentKey:0,
                markerLatLng: [47.313220, -1.319482],
                center: [47.413220, -1.219482],

                polyline: {
                    latlngs: [[47.334852, -1.509485], [47.342596, -1.328731], [47.241487, -1.190568], [47.234787, -1.358337]],
                    color: 'green',

                }
            };
        },
        methods: {


        }


    }


</script>

<style scoped>



</style>