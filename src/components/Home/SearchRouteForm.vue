<template>
    <v-card
            max-width="344"

    >
        <v-card-title style="background:#1565C0 ">
            <span style="color: aliceblue">Where To Next?</span>
        </v-card-title>
        <v-form>
            <v-container >
                <v-row justify="center" dense>
                    <v-col>
                        <v-text-field
                                label="FROM"
                                required
                        />
                    </v-col>
                    <v-spacer/>
                </v-row>
                <v-row justify="center" dense>
                    <v-col>
                        <v-text-field
                                label="TO"
                                required
                        />
                    </v-col>
                    <v-col >
                        <v-btn text width="100%">
                            <i  class="fas fa-search fa-2x" style="color: #1565C0"/>
                        </v-btn>

                    </v-col>

                </v-row>
                <v-row >
                    <v-col>
                        <v-menu
                                v-model="menu2"
                                :close-on-content-click="false"
                                :nudge-right="40"
                                transition="scale-transition"
                                offset-y
                                min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                                <v-text-field
                                        v-model="date"
                                        prepend-icon="fas fa-calendar-week"
                                        v-on="on"
                                />
                            </template>
                            <v-date-picker v-model="date" @input="menu2 = false"/>
                        </v-menu>
                    </v-col>
                    <v-col>
                        <v-menu
                                ref="menu"
                                v-model="menu3"
                                :close-on-content-click="false"
                                :nudge-right="40"
                                :return-value.sync="time"
                                transition="scale-transition"
                                offset-y
                                max-width="290px"
                                min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                                <v-text-field
                                        v-model="time"
                                        label="Select Time"
                                        readonly
                                        v-on="on"
                                />
                            </template>
                            <v-time-picker

                                    v-if="menu3"
                                    v-model="time"

                                    @click:minute="$refs.menu.save(time)"
                            />
                        </v-menu>
                    </v-col>
                </v-row>


            </v-container>
        </v-form>
    </v-card>

</template>

<script>
    export default {
        name: "SearchRouteForm",
        data: () => ({
            date: new Date().toISOString().substr(0, 10),
            modal: false,
            menu2: false,
            menu3:false,
            time:null
        })
    }
</script>

<style scoped>

</style>