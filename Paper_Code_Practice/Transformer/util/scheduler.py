from torch import optim

class LRScheduler(optim.lr_scheduler.LambdaLR):
    """ 
    논문에서 제시한 공식을 적용한 learning rate 스케줄러
    """
    def __init__(self, optimizer, d_model, warmup_steps, last_epoch=-1):

        def lr_lambda(step_num):
            if step_num == 0:
                return 1
            lrate = d_model**(-0.5) * min(step_num**(-0.5), step_num*(warmup_steps**(-1.5)))
            return lrate

        super(LRScheduler, self).__init__(optimizer, lr_lambda, last_epoch=last_epoch)