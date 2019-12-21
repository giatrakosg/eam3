<template>
    <v-card elevation="0"  color="#FAFAFA">
        <v-container fluid>
            <v-row  dense>
                <v-col >
                    <div class="font-weight-light border-bottom" style="color: #004B84; text-align: center">Route Options</div>
                </v-col>
            </v-row>
            <v-row dense align="center">
                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                           <div style="margin-bottom: -8px">Buses</div>
                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/bus.png"/>
                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/troley.png"/>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">Metro </div>
                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/metro.png"/>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">Tram</div>
                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/tram.png"/>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">Accessibility for disabled</div>
                            <i  class="fas fa-wheelchair fa-2x ml-2"/>
                        </template>

                    </v-checkbox>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <div class="font-weight-light border-bottom" style="color: #004B84; text-align: center"></div>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                <v-radio-group row>
                    <v-radio color="primary">
                        <template  v-slot:label>
                            <div style="margin-bottom: -8px">Least walk</div>
                        </template>
                    </v-radio>
                    <v-radio color="primary">
                        <template  v-slot:label>
                            <div style="margin-bottom: -8px">Fastest route</div>
                        </template>
                    </v-radio>
                    <v-radio color="primary" label="Least Changes">
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">Least Changes</div>
                        </template>
                    </v-radio>
                </v-radio-group>
                </v-col>
            </v-row>
        </v-container>
    </v-card>

</template>

<script>
    export default {
        name: "SearchRoutesOptions"
    }
</script>

<style scoped>

</style>