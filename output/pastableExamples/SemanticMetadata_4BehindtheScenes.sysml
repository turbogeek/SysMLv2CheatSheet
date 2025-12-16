// Conceptual view of what happens under the hood
// When you write:
// #engine myEngine;

// It effectively becomes:
// @engine
// part myEngine :> engines;

// Where @engine links back to the metadata definition
// allowing tools to know "This part IS an engine"
// regardless of inheritance hierarchy complexities.