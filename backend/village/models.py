from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True
class State(BaseModel):
    name = models.CharField(max_length=100,unique=True,db_index=True)
    code = models.CharField(max_length=10,unique=True)
    class Meta:
        db_table = "states"
        ordering = ["name"]
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class District(BaseModel):
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name="districts")
    name = models.CharField(max_length=100,db_index=True)
    code = models.CharField(max_length=10,blank=True,null=True)
    class Meta:
        db_table = "districts"
        ordering = ["name"]
        verbose_name = "District"
        verbose_name_plural = "Districts"

        constraints = [
            models.UniqueConstraint(
                fields=["state", "name"],
                name="unique_district_per_state"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.state.name})"


class Tehsil(BaseModel):
    district = models.ForeignKey(District,on_delete=models.CASCADE,related_name="tehsils")
    name = models.CharField(max_length=100,db_index=True)
    code = models.CharField(max_length=10,blank=True,null=True)
    class Meta:
        db_table = "tehsils"
        ordering = ["name"]
        verbose_name = "Tehsil"
        verbose_name_plural = "Tehsils"

        constraints = [
            models.UniqueConstraint(
                fields=["district", "name"],
                name="unique_tehsil_per_district"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.district.name})"


class Village(BaseModel):
    tehsil = models.ForeignKey(Tehsil, on_delete=models.CASCADE,related_name="villages")
    name = models.CharField(max_length=150,db_index=True)
    village_code = models.CharField(max_length=20,blank=True,null=True,db_index=True)
    gis_code = models.CharField(max_length=50,unique=True,blank=True,null=True,help_text="Government GIS Code (optional)")
    pincode = models.CharField(max_length=10,blank=True,null=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=7,blank=True,null=True)
    longitude = models.DecimalField(max_digits=10,decimal_places=7,blank=True,null=True)
    class Meta:
        db_table = "villages"
        ordering = ["name"]
        verbose_name = "Village"
        verbose_name_plural = "Villages"

        constraints = [
            models.UniqueConstraint(
                fields=["tehsil", "name"],
                name="unique_village_per_tehsil"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.tehsil.name})"