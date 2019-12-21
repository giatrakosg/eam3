<template>
    <v-tabs>
        <v-tab >

                Route option 1

        </v-tab>
        <v-tab-item>
            <v-container fluid lazy >
                <v-row   dense style="height: auto"  >
                    <v-col md="4" >
                        <SearchRouteDirectionTimeline />
                    </v-col>
                    <v-col md="8">
                        <SearchRoutesDirectionMap />
                    </v-col>
                </v-row>
            </v-container>
        </v-tab-item>

        <v-tab >

            Route option 1

        </v-tab>
        <v-tab-item>
            <v-container fluid lazy >
                <v-row   dense style="height: auto" >
                    <v-col md="4" >
                        <SearchRouteDirectionTimeline />
                    </v-col>
                    <v-col md="8">
                        <SearchRoutesDirectionMap />
                    </v-col>
                </v-row>
            </v-container>
        </v-tab-item>

    </v-tabs>

</template>

<script>
    import SearchRouteDirectionTimeline from "./SearchRoutesDirectionTimeline";
    import SearchRoutesDirectionMap from "./SearchRoutesDirectionMap";
    export default {
        name: "SearchRoutesDirections",
        components: {SearchRoutesDirectionMap, SearchRouteDirectionTimeline},

        data(){
            return{
                componentKey: 0,
            }

        }

    }
</script>

<style scoped>

</style>