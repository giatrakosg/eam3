<template>
    <v-card elevation="0"  color="#FAFAFA">
        <v-container fluid>
            <v-row  dense>
                <v-col >
                    <div class="font-weight-light border-bottom" style="color: #004B84; text-align: center">{{$t('text.routeoptions')}}</div>
                </v-col>
            </v-row>
            <v-row dense align="center">
                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                           <div style="margin-bottom: -8px">{{$t('text.buses')}}</div>
                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/bus.png"/>

                        </template>

                    </v-checkbox>
                </v-col>
                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">{{$t('text.trolleys')}}</div>

                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/trolley.png"/>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">{{$t('text.metro')}}</div>
                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/metro.png"/>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">{{$t('text.tram')}}</div>
                            <v-img style="margin-bottom: -10px" contain width="40px" height="40px" src="../../../assets/tram.png"/>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="primary" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">{{$t('text.accessibility')}}</div>
                            <v-icon>
                                mdi-wheelchair-accessibility
                            </v-icon>
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
                            <div style="margin-bottom: -8px">{{$t('text.leastwalk')}}</div>
                        </template>
                    </v-radio>
                    <v-radio color="primary">
                        <template  v-slot:label>
                            <div style="margin-bottom: -8px">{{$t('text.fastestroute')}}</div>
                        </template>
                    </v-radio>
                    <v-radio color="primary" label="Least Changes">
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">{{$t('text.leastchanges')}}</div>
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