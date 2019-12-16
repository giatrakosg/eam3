<template>
    <v-card
            max-width="344"
            color="#FAFAFA"
            elevation="10"

    >
        <v-card-title style="background:#1565C0 ">
            <span style="color: aliceblue">Where To Next?</span>
        </v-card-title>
        <v-form>
            <v-container fluid >
                <v-row    dense>
                    <v-col>
                        <v-text-field
                                label="FROM"
                                required
                        />
                    </v-col>
                    <v-spacer/>
                </v-row>
                <v-row align="center" dense>
                    <v-col>
                        <v-text-field
                                label="TO"
                                required
                        />
                    </v-col>
                    <v-col >
                        <v-btn text width="100%">
                            <i  class="fas fa-arrow-right fa-2x" style="color: #1565C0"/>
                        </v-btn>

                    </v-col>

                </v-row>
                <v-row align="center" dense>
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
                        <div style="height: 20">
                        <input  v-model="time" type="time"
                               required style="justify-self: center">
                        </div>
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