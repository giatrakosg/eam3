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
                    <v-checkbox    color="#004B84" hide-details >
                        <template v-slot:label>
                           <div style="margin-bottom: -8px">Buses</div>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="#004B84" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">Metro</div>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="#004B84" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">Tram</div>
                        </template>

                    </v-checkbox>
                </v-col>

                <v-col>
                    <v-checkbox    color="#004B84" hide-details >
                        <template v-slot:label>
                            <div style="margin-bottom: -8px">Accessibility for disabled</div>
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
                    <v-radio color="#004B84">
                        <template  v-slot:label>
                            <div style="margin-bottom: -8px">Least walk</div>
                        </template>
                    </v-radio>
                    <v-radio color="#004B84">
                        <template  v-slot:label>
                            <div style="margin-bottom: -8px">Fastest route</div>
                        </template>
                    </v-radio>
                    <v-radio color="#004B84" label="Least Changes">
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
        name: "SearchRoutesResultsOptions"
    }
</script>

<style scoped>

</style>