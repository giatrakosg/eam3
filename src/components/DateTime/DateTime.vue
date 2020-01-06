<template>
    <v-container>
    <v-row align="center" dense>
        <v-col>
            <v-menu
                    v-model="menu"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
            >
                <template v-slot:activator="{ on }">
                    <v-text-field
                            v-model="date"
                            v-on:keyup="emitToParentDate"
                            prepend-icon="fas fa-calendar-week"
                            v-on="on"
                    />
                </template>
                <v-date-picker v-model="date" @input="menu = false"/>
            </v-menu>
        </v-col>
        <v-col>
            <div style="height: 20px">
                <input
                        v-model="time" type="time"
                        v-on:keyup="emitToParentTime"
                        required style="justify-self: center"/>
            </div>
        </v-col>
    </v-row>
    </v-container>
</template>



<script>

    import moment from "moment";

    export default {
        name: "DateTime",
        data:() => ({
            date: new Date().toISOString().substr(0, 10),
            menu: false,
            time:""

        }),
        methods:{
            emitToParentTime(){
                this.$emit('childToParentTime',this.time)
            },
            emitToParentDate(){
                this.$emit('childToParentDate',this.date)
            }

        },
        created() {
            this.time= moment().format('HH:mm');
        }
    }
</script>

<style scoped>

</style>