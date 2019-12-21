<template>
  <div>
    <v-breadcrumbs :items="items" divider="-"></v-breadcrumbs>
  </div>
</template>

<script>
  export default {
    name : 'Breadcrumb' ,
    data: () => ({
      items: [
        {
          text: 'Dashboard',
          disabled: false,
          href: 'breadcrumbs_dashboard',
        },
        {
          text: 'Link 1',
          disabled: false,
          href: 'breadcrumbs_link_1',
        },
        {
          text: 'Link 2',
          disabled: true,
          href: 'breadcrumbs_link_2',
        },
      ],
      divider: '/',
      dividers: ['/', '\\', '.', ';', '>', '-'],
      large: false,
      customDiv: false,
    }),
  }
</script>

<style lang="css" scoped>
</style>
