<template lang="html">
  <div class="">
  <v-row align="center">
    <v-card
      class="mx-auto"
      max-width="400"
      tile
    >
      <v-list
        :disabled="disabled"
        :dense="dense"
        :two-line="twoLine"
        :three-line="threeLine"
        :shaped="shaped"
        :flat="flat"
        :subheader="subheader"
        :sub-group="subGroup"
        :nav="nav"
        :avatar="avatar"
        :rounded="rounded"
      >
        <v-subheader
        >
            ΚΑΘΥΣΤΕΡΗΣΕΙΣ
        </v-subheader>
        <v-list-item-group v-model="item" color="primary">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :inactive="inactive"
          >
            <v-list-item-avatar v-if="avatar">
              <v-img :src="item.avatar"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-subtitle v-if="twoLine || threeLine" v-html="item.subtitle"></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-row>
  </div>
</template>

<script>
import moment from 'moment';
export default {
  name : 'Traffic' ,
  data () {
    return {
      timestamp : '' ,
      value : true ,
      item: 5,
      items: [
        {
          avatar: 'https://i.pinimg.com/originals/02/b7/04/02b704dcc8cb5084a806f2915acb23af.jpg',
          title: 'Διακοπη Λειτουργιας Μετρο',
          subtitle: "<span class='text--primary'>Γραμμη 2</span> &mdash; Λογω εργασιων η γραμμη 2 του μετρο θα παραμεινει κλειστη",
        },
        {
          avatar: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Bus-logo.svg/454px-Bus-logo.svg.png',
          title: 'Καθυστερησεις γραμμη 136,137',
          subtitle: "<span class='text--primary'>136-137</span> &mdash; Καθυστερησεις στις γραμμες 136-137 λογω συμφορησης",
        },
        {
          avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeH8EeTz-89gZSd86VekUrwuRJDkVhzmzz6LrDi7lC1gj1D1zF3w&s',
          title: 'Διακοπη Λειτουργιας Τραμ',
          subtitle: "<span class='text--primary'>Σταση Φιξ εως Συνταγμα</span> &mdash; Δεν πραγματοποιουνται δρομολογια απο τις στασεις Φιξ εως και Συνταγμα",
        },
        {
          avatar: 'https://i.pinimg.com/originals/02/b7/04/02b704dcc8cb5084a806f2915acb23af.jpg',
          title: 'Μη Λειτουργια ανελκυστηρα',
          subtitle: "<span class='text--primary'>Σταση Ευαγγελισμος</span> &mdash; Δεν ειναι σε λειτουργια ο ανελκυστηρας στην σταση Ευαγγελισμος",
        },
      ],
      disabled: false,
      dense: false,
      twoLine: false,
      threeLine: true,
      shaped: false,
      flat: false,
      subheader: false,
      inactive: false,
      subGroup: false,
      nav: false,
      avatar: true,
      rounded: false,
    }
  },
  created() {
      setInterval(this.getNow, 1000);
  },
  methods: {
      getNow: function() {
          this.timestamp = moment().format('h:mm');
      }
  }

}
</script>

<style lang="css" scoped>
</style>
