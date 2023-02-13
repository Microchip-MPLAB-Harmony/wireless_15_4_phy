# qmm_queue_init Function

## C

```c
void qmm_queue_init(queue_t *q, uint8_t capacity)
```

## Summary

Initializes the queue  

## Description

This function initializes the queue. Note that this function
should be called before invoking any other functionality of QMM.

## Precondition

None  

## Parameters

| Param | Description |
|:----- |:----------- |
| q | The queue which should be initialized |
| capacity | Queue length (Max No of buffers which can be accomodated in the queue)  

## Returns

None.  

## Example

```c
queue_t app_queue;
uint8_t queue_size = 10;
qmm_queue_init(&app_queue, queue_size);
```

## Remarks

None 

